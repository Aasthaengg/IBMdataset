# solution

nim, mike= map(int, input().split())
if 2*nim>=mike:
  data=mike//2
else:
  data=nim+(mike-2*nim)//4
print(data)