import sys
input = sys.stdin.readline
x,y,a,b,c = map(int,input().split())
red = list(map(int,input().split()))+[0]
green = list(map(int,input().split()))+[0]
cless = list(map(int,input().split()))+[0]
red.sort(reverse = True)
green.sort(reverse = True)
cless.sort(reverse = True)
red_ind = 0
green_ind = 0
cless_ind = 0
ans = 0
for _ in range(x+y):
    if red_ind == x:
        red_ind = a
    if green_ind == y:
        green_ind = b
    if max(red[red_ind],green[green_ind],cless[cless_ind]) == red[red_ind]:
        ans += red[red_ind]
        red_ind += 1
    elif max(red[red_ind],green[green_ind],cless[cless_ind]) == green[green_ind]:
        ans += green[green_ind]
        green_ind += 1
    else:
        ans += cless[cless_ind]
        cless_ind += 1

print(ans)
