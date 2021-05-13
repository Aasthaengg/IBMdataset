N = int(input())
B = list(map(int,input().split()))

C = [B[0]]

[C.append(min(B[x],B[x-1])) for x in range(1,N-1)]

C.append(B[N-2])

print(sum(C))
