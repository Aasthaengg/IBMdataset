n = int(input())

al = ['a','b','c','d','e','f','g','h','i','j']
w = ['a']

for num in range(n-1):
    x = []
    for i in range(len(w)):
        x.append(w[i] + 'a')
        for num in range(num+1):
            if al[num] in w[i]:
                x.append(w[i] + al[num+1])
    w = x

for _ in range(len(w)):
    print(w[_])