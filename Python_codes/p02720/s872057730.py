from collections import deque
K = int(input())
A = deque([str(i) for i in range(1,10)])
cnt = 0
while cnt<K:
    a = A.popleft()
    cnt += 1
    if a[-1]=="0":
        a0 = a+"0"
        a1 = a+"1"
        A.append(a0)
        A.append(a1)
    elif a[-1]=="9":
        a0 = a+"8"
        a1 = a+"9"
        A.append(a0)
        A.append(a1)
    else:
        b = a[-1]
        a0 = a+str(int(b)-1)
        a1 = a+b
        a2 = a+str(int(b)+1)
        A.append(a0)
        A.append(a1)
        A.append(a2)
print(a)