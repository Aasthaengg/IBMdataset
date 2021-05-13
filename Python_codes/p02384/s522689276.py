def whatIsRight(u,f):	
    r = 0
    if u == 1:
        if f == 2:
            r = 3
        elif f == 3:
            r = 5
        elif f == 4:
            r = 2
        elif f == 5:
            r = 4
	
    elif u == 2:
        if f == 6:
            r = 3
        elif f == 3:
            r = 1
        elif f == 1:
            r = 4
        elif f == 4:
            r = 6

    elif u == 3:
        if f == 5:
            r = 1
        elif f == 1:
            r = 2
        elif f == 2:
            r = 6
        elif f == 6:
            r = 5
			
    elif u == 4:
        if f == 6:
            r = 2
        elif f == 2:
            r = 1
        elif f == 1:
            r = 5
        elif f == 5:
            r = 6 
			
    elif u == 5:
        if f == 3:
            r = 6
        elif f == 6:
            r = 4
        elif f == 4:
            r = 1
        elif f == 1:
            r = 3
		
    elif u == 6:
        if f == 5:
            r = 3
        elif f == 3:
            r = 2
        elif f == 2:
            r = 4
        elif f == 4:
            r = 5
    return r
			
n = list(map(int,input().split()))
N = int(input())

for i in range(N):
    m = list(map(int,input().split()))
    num = []

    for j in range(len(m)):
        for k in range(len(n)):
            if m[j] == n[k]:
                num.append(k+1)
                break
	
    print(n[whatIsRight(num[0],num[1]) -1])