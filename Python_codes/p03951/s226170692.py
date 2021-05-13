N = int(input())
s = str(input())
t = str(input())

if s == t:
    print(N)
else:
    for i in range(N,0,-1):
        #print(s[N-i:],t[0:i],)
        if s[N-i:]==t[0:i]:
            print(2*N-i)
            break
    else:
        print(2*N)