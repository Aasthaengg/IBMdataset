X=5*10**15
S = input()
k = int(input())

if all(S[i]=='1' for i in range(k)):
    print('1')
else:
    for i in range(k):
        if S[i]!='1':
            print(S[i])
            break
