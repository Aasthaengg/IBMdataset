def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

N,A,B=map(int,input().split())
v=list(map(int,input().split()))
v.sort()
maxsum=0
for i in range(0,A):
    maxsum+=v[N-1-i]
maxaverage=((maxsum*(10**6))//A)/(10**6)

s=v[N-A]
count1=0
count2=0
for i in range(0,A):
    if v[N-1-i]==s:
        count1+=1
for i in range(0,N):
    if v[i]==s:
        count2+=1
if count1!=A:
    way=factorial(count2)//(factorial(count1)*factorial(count2-count1))
    print(maxaverage)
    print(way)
else:
    way=0
    for i in range(A,min(count2,B)+1):
        way+=factorial(count2)//(factorial(i)*factorial(count2-i))
    print(maxaverage)
    print(way)
