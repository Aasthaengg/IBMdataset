from itertools import accumulate
def main():
    n,k = map(int, input().split())
    s = list(input())
    ls = []

    cnt = 0
    buf = '1'
    for ele in s:
        if ele != buf:
            ls.append(cnt)
            cnt = 1
            buf = ele
        else:
            cnt += 1
    ls.append(cnt)

    if buf == '0':
          ls.append(0)

    w = 2*k+1
    if w >= len(ls):
          print(n)
    else:
          acc = [0] + list(accumulate(ls))
          ans = 0
          for i in range(0,len(ls)-w+1,2):
               ans = max(ans,acc[i+w]-acc[i])
          print(ans)

main()