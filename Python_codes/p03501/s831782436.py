parking_time, time_price, anytime_price = map(int, input().split())

min_price_plan = min(parking_time * time_price, anytime_price)

print(min_price_plan)
