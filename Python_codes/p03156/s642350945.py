n = int(input())
a, b = map(int, input().split())
li_p = list(map(int, input().split()))

print(
    min(
        len(list(filter(lambda x: x <= a, li_p))),
        len(list(filter(lambda x: (a + 1) <= x <= b, li_p))),
        len(list(filter(lambda x: (b + 1) <= x, li_p))),
    )
)

