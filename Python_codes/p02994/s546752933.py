N,L = list(map(int,input().split()))
app_taste = list(range(L,L+N))
bite_apple=L
for i in app_taste:
    if abs(bite_apple) > abs(i):
        bite_apple = i
print(sum(app_taste) - bite_apple)

