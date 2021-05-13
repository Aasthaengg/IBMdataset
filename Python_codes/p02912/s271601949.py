import bisect
 
N,M = map(int,input().split())
Price_List = list(map(int,input().split()))
Price_List.sort()
for i in range(M):
    New_Price = Price_List.pop(-1)//2
    Price_List.insert(bisect.bisect(Price_List,New_Price),New_Price)
print(sum(Price_List))