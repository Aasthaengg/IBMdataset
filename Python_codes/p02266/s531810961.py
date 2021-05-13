tochi=input()
s=[]
I=[]

sum=0
n=len(tochi)
for i in range(n):
    if tochi[i] == "\\":
        s.append(i)
    elif tochi[i] == "/" and s:
        j = s.pop()
        a = i - j
        sum += a
	
        while I and I[-1][0] > j:
            a += I.pop()[1]
        I.append([j, a])

print(sum)
print(len(I), *(a for j, a in I))
    

