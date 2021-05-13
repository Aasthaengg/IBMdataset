n,k,q = map(int,input().split())
player = [0] * n
for i in range(q):
    player[int(input())-1] += 1
result = ['Yes' if k - q + player[i] > 0 else 'No' for i in range(n)]
for i in result:
    print(i)
