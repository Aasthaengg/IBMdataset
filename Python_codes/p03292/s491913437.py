list1 = sorted(map(int,input().split()))
print(sum([abs(list1[i]-list1[i+1]) for i in range(0,len(list1)-1)]))