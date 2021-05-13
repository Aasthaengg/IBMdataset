a, b, k = map(int, input().split())
if (b-a+1) <= 2 * k :
    count = a
    while count <= b :
        print(count)
        count += 1
else :
    for i in range(k) :
        print(a+i)
    for i in range(k) :
        print(b-((k-1)-i))
