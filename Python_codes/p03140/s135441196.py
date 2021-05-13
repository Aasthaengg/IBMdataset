n=int(input())
a= list(input())
b= list(input())
c= list(input())

alphabet = [chr(i) for i in range(97, 97+26)]

ans = 0
for i in range(n):
    cnt = 200
    for j in range(26):
        cnt_tmp = 0
        if (a[i] != alphabet[j]):
            cnt_tmp += 1
        if (b[i] != alphabet[j]):
            cnt_tmp += 1
        if (c[i] != alphabet[j]):
            cnt_tmp += 1
        cnt = min(cnt, cnt_tmp)
    ans += cnt

print(ans)
    
        
        

'''
west
east
wait
'''



