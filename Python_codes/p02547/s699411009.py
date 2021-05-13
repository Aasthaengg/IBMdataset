from collections import deque

target_1 = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
def func(a=deque() , targetlist=target_1):
    x1 = a.count(targetlist[0])
    x2 = a.count(targetlist[1])
    x3 = a.count(targetlist[2])
    x4 = a.count(targetlist[3])
    x5 = a.count(targetlist[4])
    x6 = a.count(targetlist[5])
    if((x1+x2+x3+x4+x5+x6)==3):
        return True
    else:
        return False

N = int(input())
D_array = [list(map(int, input().split())) for i in range(N)]
Q = deque([[0] * 2 for i in range(3)])

j = 0
ans = 0
while j < N:
    Q.pop()
    Q.appendleft(D_array[j])
    if(func(Q,target_1)):
        print("Yes")
        ans = 1
        break
    else:
        j = j+1

if(ans==0):print("No")

