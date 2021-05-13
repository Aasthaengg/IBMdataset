n = int(input())
a = list(map(int,input().split()))
count = 0
s = []

def find_i():
    for i in range(n):
        if a[i] == max(a):
            return i+1
        
def find_m():
    for i in range(n):
        if a[i] == min(a):
            return i+1
        
maxi = find_i()
mini = find_m()

if min(a) < 0:
    if abs(min(a)) <= abs(max(a)):
        for _ in range(n):
            a[_] += max(a)
            s.append(str(maxi) + ' ' + str(_+1))
            count += 1
        for i in range(n-1):
            a[i+1] += a[i]
            s.append(str(i+1) + ' ' + str(i+2))
            count += 1
            
    else:
        for _ in range(n):
            a[_] += min(a)
            s.append(str(mini) + ' ' + str(_+1))
            count += 1
        for i in range(n-2,-1,-1):
            a[i] += a[i+1]
            s.append(str(i+2) + ' ' + str(i+1))
            count += 1

else:
    for i in range(n-1):
        a[i+1] += a[i]
        s.append(str(i+1) + ' ' + str(i+2))
        count += 1
print(count)
for i in range(len(s)):
    print (s[i])