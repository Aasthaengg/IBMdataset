n=[int(input()) for _ in range(int(input()))]
N1,N2=max(n),sorted(n)[-2]
[print(N2) if i==N1 else print(N1) for i in n]