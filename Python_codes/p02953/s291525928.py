N = int(input())
H = list(map(int,input().split()))
i = 0
H[0] -= 1

while True:
    if N == 1:
        answer = 'Yes'
        break
    if H[i]<H[i+1]:
        H[i+1] -= 1
    if H[i]>H[i+1]:
        answer = 'No'
        break
    i += 1
    if i == N-1:
        answer = 'Yes'
        break
print(answer)