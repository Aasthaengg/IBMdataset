n=int(input())
a= list(input())
b= list(input())
c= list(input())

ans = 0
for i in range(n):
    ans += len({a[i], b[i], c[i]}) - 1

print(ans)
    
        
        

'''
west
east
wait

{'w', 'e', 'w'}
{'w', 'e'}
len → 2 
1文字は使って良い -1


'''