n, Lxy = int(input()),\
         [abs(x - y) for x, y in zip( list(map(int, input().split())),
                                      list(map(int, input().split())) )]
print(sum(Lxy))
print((sum([d**2 for d in Lxy])**(1/2)))
print((sum([d**3 for d in Lxy])**(1/3)))
print(max(Lxy))