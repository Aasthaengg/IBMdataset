N = int(input())
kotae = 0
for i in range(0,N+1):
    if i%3 == 0 or  i%5 == 0:
        kotae = kotae
    else:
        kotae = kotae + i
print(kotae)