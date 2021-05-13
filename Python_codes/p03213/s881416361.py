N=int(input())
numbers = {2: 0, 3: 0, 5: 0,7: 0, 11: 0, 13: 0, 17: 0, 19: 0, 23: 0, 29: 0, 31: 0, 37: 0, 41: 0, 43: 0, 47: 0, 53: 0, 59: 0, 61: 0, 67: 0, 71: 0, 73: 0, 79: 0, 83: 0, 89: 0, 97: 0}
prime = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
for n in range(2,N+1):
    a=n
    while(a!=1):
        for j in prime:
            if(a%j==0):
                numbers[j]+=1
                a/=j
n75 = 0
n25 = 0
n15 = 0
n5=0
n3 = 0 
for i in numbers.values():
    if i>=74:
        n75+=1
    if i>=24:
        n25+=1
    if i>=14:
        n15+=1
    if i>= 4:
        n5+=1
    if i>=2:
        n3+=1
ans = n75+n25*(n3-1)+n15*(n5-1)+n5*(n5-1)//2*(n3-2)
print(str(ans)+"\n")