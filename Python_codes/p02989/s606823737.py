n=int(input())
l1=list(map(int, input().split()))
l2=sorted(l1)
print(l2[int(len(l1)/2)]-l2[int(len(l1)/2-1)])





#上は含みつつ、↓は含まない想定ね