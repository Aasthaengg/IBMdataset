N = int(input())
A = list(map(int, input().split()))
flag = 0
List = []

for n in range(N):
    if A[n]%2 == 0:
        List.append(A[n])


for n in range(len(List)):
    if List[n] % 3 == 0:
        pass
    elif List[n] % 5 == 0:
        pass
    else:
        flag += 1
        break

if flag != 0:
    print("DENIED")
else:
    print("APPROVED")