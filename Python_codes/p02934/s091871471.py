#https://atcoder.jp/contests/abc138/tasks/abc138_b
N = int(input())
N_List = sum(map(lambda x:1/x ,list(map(int,input().split()))))
print(1/N_List)