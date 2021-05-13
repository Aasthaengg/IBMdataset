a,b=map(str,input().split())
ans_list=[]
ans_list.append(''.join([a]*int(b)))
ans_list.append(''.join([b]*int(a)))
ans_list.sort()
print(ans_list[0])