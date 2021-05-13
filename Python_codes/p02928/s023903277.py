# B - Kleene Inversion
from typing import Optional, Sequence


class BinaryIndexedTree:
    """Binary Indexed Tree (Fenwick Tree)
    Each operation runs in O(logN).

    References:
        http://hos.ac/slides/20140319_bit.pdf
    """

    __slots__ = ["_size", "_tree", "is_zero_origin"]

    def __init__(
        self,
        size: int,
        initial_values: Optional[Sequence[int]] = None,
        is_zero_origin: bool = True,
    ):
        self._size = size
        self._tree = [0] * (size + 1)
        self.is_zero_origin = is_zero_origin
        if initial_values:
            self._build(initial_values)

    def _build(self, initial_values: Sequence[int]):
        for i, a in enumerate(initial_values):
            self.add(i, a)

    def add(self, index: int, value: int) -> None:
        """Add value to tree[index], O(logN)."""
        if self.is_zero_origin:
            index += 1
        while index <= self._size:
            self._tree[index] += value
            index += index & -index

    def sum(self, index: int) -> int:
        """Return the sum of [1, index] in O(logN)."""
        ret = 0
        while index > 0:
            ret += self._tree[index]
            index -= index & -index
        return ret

    def range_sum(self, left: int, right: int) -> int:
        """Return the range sum of [left, right] in O(logN)."""
        if not self.is_zero_origin:
            left -= 1
        return self.sum(right) - self.sum(left)


def main():
    N, K, *A = map(int, open(0).read().split())
    tree = BinaryIndexedTree(2000, is_zero_origin=False)
    x = 0
    for i, a in enumerate(A, 1):  # internal inversion
        tree.add(a, 1)
        x += i - tree.sum(a)
    y = -x
    for i, a in enumerate(A, 1):  # external inversion
        tree.add(a, 1)
        y += i + N - tree.sum(a)
    MOD = 10 ** 9 + 7
    print((x * K + y * K * (K - 1) // 2) % MOD)


if __name__ == "__main__":
    main()
