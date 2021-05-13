N, A, B = (int(x) for x in input().split())
Ans = [i if A <= sum(int(x) for x in list(str(i))) <= B else 0 for i in range(1,N+1)]
print(sum(Ans))