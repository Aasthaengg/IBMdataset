n,m=map(int,input().split())
a_list=map(int,input().split())
mod_count={0:1}
mod_sum = 0
for a in a_list:
    mod_sum = (mod_sum + a) % m
    mod_count[mod_sum] = mod_count.get(mod_sum,0) + 1
    
ans = 0
for i in mod_count.values():
    ans += i*(i-1)//2
    
print(ans)