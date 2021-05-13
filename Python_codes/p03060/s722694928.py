#https://atcoder.jp/contests/abc125/tasks/abc125_b
N = int(input())
X_List = list(map(int,input().split()))
Y_List = list(map(int,input().split()))
XY_List = [X_List[i]-Y_List[i] for i in range(N)]
print(sum(list(map(lambda x:x if x>= 0 else 0,XY_List))))