a,b = map(int,input().split())

for i in range(2,1000):
    tmp_a = sum(range(1,i)) - a
    tmp_b = sum(range(1,i+1)) - b
    if tmp_a == tmp_b:
        print(tmp_a)
        break