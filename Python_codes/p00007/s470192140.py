import math

n,dbt = int(input()),100
for i in range(n):
    dbt = math.ceil(dbt*1.05)
print(dbt*1000)