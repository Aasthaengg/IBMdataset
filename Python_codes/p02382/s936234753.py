n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
Distance = [abs(xi-yi) for (xi,yi) in zip(x,y)]
print(sum(Distance))#マンハッタン距離
Euclid=[i**2 for i in Distance]
print(sum(Euclid)**0.5)
wa = [i**3 for i in Distance]
print(sum(wa)**(1/3))
print(max(Distance))

