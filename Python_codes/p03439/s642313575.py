import sys

#N = 5
#ss = ['W', 'Vacant', 'W', 'Vacant', 'M']

def judge(x):
    print(x)
    sys.stdout.flush()
    s = input()
    #s = ss[x]
    
    if s=='Vacant':
        print(x)
        exit()
        
    if x%2==0 and s!=ini_s:
        return True
    elif x%2==1 and s==ini_s:
        return True
    else:
        return False

N = int(input())
print(0)
sys.stdout.flush()
ini_s = input()
#ini_s = ss[0]

if ini_s=='Vacant':
    print(0)
    exit()

print(N-1)
sys.stdout.flush()
last_s = input()
#last_s = ss[N-1]

if last_s=='Vacant':
    print(N-1)
    exit()

l, r = 1, N-1
    
while l<=r:
    m = (l+r)//2
        
    if judge(m):
        r = m-1
    else:
        l = m+1

print(l-1)
exit()