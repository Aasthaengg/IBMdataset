import math

S = int(input())

mod = 10 ** 9 + 7

max_length = S // 3  # because each of items must be greater than or equal to 3

ans = 0
for length in range(1, max_length + 1):
    # Subtracting 3 from each of items reduces S by 3 * length.
    # Now each of items are greater than or equal to 0.
    s = S - 3 * length

    # Consider a combination with repetition given:
    #  - "|" x (length - 1)
    #  - "o" x s
    # For example, if length = 2 and s = 3,
    #  | o o o  := {0, 3}
    #  o | o o  := {1, 2}
    #  o o | o  := {2, 1}
    #  o o o |  := {3, 0}
    # -> The answer is 4.
    c = math.factorial(s + length - 1) // (math.factorial(s) * math.factorial(length - 1))
    ans = (ans + c) % mod

print(ans)
