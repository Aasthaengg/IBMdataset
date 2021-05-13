N = int(input())
numbers = list(map(int, input().split()))

odds = list(filter(lambda x: x % 2 == 0, numbers))
evens = list(filter(lambda x: x % 2 == 1, numbers))

# evens_from_odds = sum(divmod(len(odds), 2))
# odds_from_evens = sum(divmod(len(evens), 2))
odds_from_evens = int(len(evens) / 2)
evens_mod = len(evens) % 2
if evens_mod == 1:
    print("NO")
else:
    print("YES")