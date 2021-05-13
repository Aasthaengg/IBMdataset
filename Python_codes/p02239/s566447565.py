#coding:utf-8
                
def BFS(i,A,d,dist):
    dist[i]=d
    for point in A[i]:
        if dist[point-1]==-1 or dist[point-1]>d+1:
            BFS(point-1,A,d+1,dist)

if __name__=="__main__":
    n=int(input())
    A=[]
    for i in range(n):
        A.append(list(map(int,input().split(" ")))[2:])
    dist=[-1]*n
    BFS(0,A,0,dist)

    for i in range(n):
        print("{} {}".format(i+1,dist[i]))