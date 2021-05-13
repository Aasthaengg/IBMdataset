def cin():
	return map(int,input().split())

def cino(test=False):
    if not test:
        return int(input())
    else:
        return input()
def cina():
  return list(map(int,input().split()))

a = cino()
b = cino()
c = cino()
d = cino()

ans = min(a,b)*c + (a-min(a,b))*d
print(ans)
# a = list(a)
# has = {}
# x,y = -1,-1
# for i in range(len(a)):
#     has[a[i]]=[0,0]

# for i in range(len(a)):
#     has[a[i]][0] += 1
#     if has[a[i]][0]==1:
#         has[a[i]][1] = i
#     temp1 = has[a[i]][0]
#     # print(temp1)
#     if i>2 and temp1>2:
#         temp = has[a[i]][1]
#         if temp1>(i-temp)//2:
#             x,y = temp+1,i+1
#             break
# print(x,y)


