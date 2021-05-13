N = int(input())
C =  int(N/1.08)
flag = False
for i in range(0, 2):
    if int((C+i)*1.08) == N:
        print(C+i)
        flag = True
if not flag:
    print(":(")