A = input()

count = [0]*26

ans = 1
count[ord(A[0])-97]+=1

for i in range(1,len(A)):
    ans += i-count[ord(A[i])-97]
    count[ord(A[i])-97]+=1

print(ans)