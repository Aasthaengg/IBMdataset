def a_dividing_a_string():
    S = input()

    previous = ''
    ans = 0
    for ch in S:
        if len(previous) == 2:  # ch を分割とすれば条件を満たす
            ans += 1
            previous = ''
        elif len(previous) == 1:
            if ch == previous:  # previous + ch を分割とせねば条件を満たせない
                previous += ch
            else:
                ans += 1  # previous と ch はそれぞれで分割とすればいい
                previous = ch
        else:  # ch を分割とすれば条件を満たす (次の文字のために ch を足しておく)
            ans += 1
            previous = ch
    return ans

print(a_dividing_a_string())