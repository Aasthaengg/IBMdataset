N = int(input())
if N == 1:
    print('Yes')
    print('2')
    print('1 1')
    print('1 1')
    exit()
for subs in range(2, N):
    n = N - subs
    if n == subs*(subs-1) // 2:
        print("Yes")
        print(subs+1)
        print(subs, end='')
        for i in range(1, subs+1):
            print(' ', end='')
            print(i, end='')
        print()
        li = [[] for _ in range(subs)]
        num = subs+1
        for i in range(len(li)):
            for j in range(i+1, subs):
                li[i].append(num)
                li[j].append(num)
                num += 1
        for ll in range(len(li)):
            print(len(li[ll])+1, end=' ')
            print(ll+1, end='')
            for kk in li[ll]:
                print(' ' + str(kk), end='')
            print()
        exit()
print("No")



