jisho= {0:
    [[1,2],[3,1],[4,3],[2,4]],
     1:
    [[0,3],[3,5],[5,2],[2,0]],
    2:
    [[0,1],[1,5],[5,4],[4,0]],
    3:
    [[0,4],[4,5],[5,1],[1,0]],
    4:
    [[0,2],[2,5],[5,3],[3,0]],
    5:
    [[2,1],[1,3],[3,4],[4,2]]
       }
i_number = [int(x) for x in input().split()]
n = int(input())
for _ in range(n):
    q1,q2 = [int(x) for x in input().split()]
    for i,n in enumerate(i_number):
        if q1 == n:
            qq1 = i
        if q2 == n:
            qq2 = i
    for k,v in jisho.items():
        if [qq1,qq2] in v:
            print(i_number[k])

