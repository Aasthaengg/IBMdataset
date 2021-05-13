from collections import deque
from collections import OrderedDict

def main():
    N, *AB = map(int, open(0).read().split())
    C = [0]*N
    ans = 0
    for i in range(N):
        a = AB[i * 2 + 0]
        b = AB[i * 2 + 1]
        C[i] = a + b
        ans -= b
    C.sort(reverse=True)
    eaten = (N + 1) // 2
    for i in range(eaten):
        ans += C[2*i]
    print(ans)

if __name__ == '__main__':
    main()
