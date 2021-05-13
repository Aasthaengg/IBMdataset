import collections

N = int(input())
D = collections.Counter(list(map(int,input().split())))
M = int(input())
T = list(map(int,input().split()))

if M > N :
    print("NO")
    exit()

# print(D)
for i in range(M):
    # print(D[T[i]])
    if D[T[i]] == 0:
        print("NO")
        exit()
    D[T[i]] -= 1
    # print(D[T[i]])
    
print("YES")