N = int(input())
alp_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = []
 
for i in range(1,12):
  if N <= 26 ** i:
    N -= 1
    for j in range(i):
      ans.append(alp_list[N % 26])
      N  = N // 26
    break
  else:
    N -= 26 ** i
ans.reverse()
print("".join(ans)) 