li = list(map(int,input().split()))
ok = (li[0]-li[2]) if li[2]==0 else (li[0]-li[2])*2
a = (li[1]-1)*ok/(li[0]*li[0])
print("{:.10f}".format(a))