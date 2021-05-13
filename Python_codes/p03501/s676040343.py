hours, price_per_h, fixed_charge = map(int, input().split())

plan_a = hours * price_per_h

if plan_a >= fixed_charge:
    print(fixed_charge)
elif plan_a < fixed_charge:
    print(plan_a)