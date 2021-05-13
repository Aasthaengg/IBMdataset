list1 = list( map(int, input().split()) ) 
A,B = list1[0], list1[1] #A個口の電源タップを使って差し込み口をB個作りたい。

x = 1 #現在の差込口の数
count = 0 #電源タップを差し込んだ回数

while x < B:
    x += (A - 1)
    count += 1

print(count)
